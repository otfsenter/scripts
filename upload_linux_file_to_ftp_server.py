import ftplib
import os
import socket
import sys

import datetime
import my_key
import paramiko


def connect(server_ftp, ftp_username, ftp_password):
    try:
        ftp = ftplib.FTP(server_ftp)
        ftp.login(user=ftp_username, passwd=ftp_password)
        print('connected to: "%s"' % server_ftp)
        return ftp
    except (socket.error, socket.gaierror):
        print("FTP login failed, please check hostname, username or password")
        sys.exit(0)


def disconnect(ftp):
    ftp.quit()


def upload(ftp, file_path, buffer_size):
    f = open(file_path, "rb")
    file_name = os.path.split(file_path)[-1]
    try:
        ftp.storbinary('STOR %s' % file_name, f, buffer_size)
        print('upload "%s" successfully' % file_name)
    except ftplib.error_perm:
        return False
    return True


def download(ftp, filename, buffer_size):
    f = open(filename, "wb").write
    try:
        ftp.retrbinary("RETR %s" % filename, f, buffer_size)
        print('download "%s" successfully' % filename)
    except ftplib.error_perm:
        return False
    return True


def list_info(ftp):
    ftp.dir()


def find(ftp, filename):
    ftp_f_list = ftp.nlst()
    if filename in ftp_f_list:
        return True
    else:
        return False


def mk_dir(ftp, path):
    try:
        ftp.mkd(path)
    except ftplib.error_perm:
        print("directory is existed or can not create")


def change_dir(ftp, path):
    try:
        ftp.cwd(path)
    except ftplib.error_perm:
        print('can not access "%s"' % path)


def year_month_day():
    now = str(datetime.datetime.now())
    return now.split(' ')[0].replace('-', '')

def upload_to_ftp(name_ftp, username_ftp, password_ftp, buffer_size, name_server, path_local, need_file_list):

    ftp = connect(name_ftp, username_ftp, password_ftp)

    # TODO: only test
    change_dir(ftp, 'test')  # only test

    mk_dir(ftp, year_month_day())
    change_dir(ftp, year_month_day())

    mk_dir(ftp, name_server)
    change_dir(ftp, name_server)

    print(f'current directory: {ftp.pwd()}')

    for each_file in need_file_list:
        file_absolute_path = os.path.join(path_local, each_file)
        upload(ftp, file_absolute_path, buffer_size)

    # ftp.rename("test.txt", filename)
    # if os.path.exists(filename):
    #     os.unlink(filename)
    #
    # download(ftp, filename)

    ftp.quit()


def server_file_list(server_name, server_username, server_password, remote_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server_name, 22, server_username, server_password)
        std_in, stdout, stderr = ssh.exec_command('cd %s; ls' % remote_path)
        output = stdout.readlines()
        output = [str(i).strip() for i in output]
        return output
    except paramiko.ssh_exception.AuthenticationException:
        print(f'{server_name} invalid username or password')
        return False


def analyze_server_file_list(keyword, file_list):
    keyword_list = []
    for i in file_list:
        if keyword in i:
            keyword_list.append(i)
    return keyword_list

def remote_scp(server_name, remote_path, local_path, file_name, username, password):
    if not os.path.isdir():
        os.makedirs(local_path)

    local_file_path = os.path.join(local_path, file_name)
    if not os.path.isfile(local_file_path):
        with open(local_file_path, 'w'):
            pass

    t = paramiko.Transport(sock='%s:22' % server_name)
    t.connect(username=username, password=password)

    sftp paramiko.SFTPClient.from_transport(t)
    src = remote_path + '/' + file_name
    des = os.path.join(local_path, file_name)
    sftp.get(src, des)
    t.close()


def get_file_list_from_server(server_name, server_username, server_password, remote_path, keyword):
    file_list = server_file_list(server_name, server_username, server_password, remote_path)
    keyword_list = analyze_server_file_list(keyword, file_list)
    return keyword_list


def download_from_server(name_server, path_remote, path_local, need_file_list, username_server, password_server):
    if path_remote.endswith('/'):
        path_remote = path_remote[:len(path_remote) - 1]

    if not os.path.isdir(path_local):
        os.makedirs(path_local)

    for each_file in need_file_list:
        local_file_path = os.path.join(path_local, each_file)
        if not os.path.isfile(local_file_path):
            with open(local_file_path, 'w'):
                pass

    t = paramiko.Transport(sock='%s:22' % name_server)
    t.connect(username=username_server, password=password_server)
    sftp = paramiko.SFTPClient.from_transport(t)

    for each_file in need_file_list:
        src = path_remote + '/' + each_file
        des = os.path.join(path_local, each_file)
        sftp.get(src, des)

    t.close()

def remove_local_file(path_local, need_file_list):
    for each_file in need_file_list:
        a = os.path.join(path_local, each_file)
        os.unlink(a)


def host_username_password(file_password):
    token_list = []
    with open(file_password, 'r') as f:
        for i in f:
            host, _, username, password, _, _, _, _ = i.strip().split('|')
            token_list.append([host, username, password])
    return token_list


def main():
    name_server = ''
    username_server = ''
    password_server = ''
    path_remote = ''
    keyword = '201803'
    path_local = r'D:\PycharmProjects\ftp'

    name_ftp = 'ftp.aliyun.com'
    username_ftp = my_key.itoc_account
    password_ftp = my_key.itoc_password
    buffer_size = 8192

    need_file_list = get_file_list_from_server(name_server, username_server, password_server, path_remote, keyword)
    # print(need_file_list)

    download_from_server(name_server, path_remote, path_local, need_file_list, username_server, password_server)

    upload_to_ftp(name_ftp, username_ftp, password_ftp, buffer_size, name_server, path_local, need_file_list)
    #
    remove_local_file(path_local, need_file_list)


if __name__ == '__main__':
    main()
