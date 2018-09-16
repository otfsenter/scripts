if v:lang =~ "utf8$" || v:lang =~ "UTF-8$"
   set fileencodings=ucs-bom,utf-8,latin1
endif

set nocompatible	" Use Vim defaults (much better!)
filetype plugin on
set bs=indent,eol,start		" allow backspacing over everything in insert mode
"set ai			" always set autoindenting on
"set backup		" keep a backup file
set viminfo='20,\"50	" read/write a .viminfo file, don't store more
			" than 50 lines of registers
set history=50		" keep 50 lines of command line history
set ruler		" show the cursor position all the time

" Only do this part when compiled with support for autocommands
if has("autocmd")
  augroup redhat
  autocmd!
  " In text files, always limit the width of text to 78 characters
  " autocmd BufRead *.txt set tw=78
  " When editing a file, always jump to the last cursor position
  autocmd BufReadPost *
  \ if line("'\"") > 0 && line ("'\"") <= line("$") |
  \   exe "normal! g'\"" |
  \ endif
  " don't write swapfile on most commonly used directories for NFS mounts or USB sticks
  autocmd BufNewFile,BufReadPre /media/*,/run/media/*,/mnt/* set directory=~/tmp,/var/tmp,/tmp
  " start with spec file template
  autocmd BufNewFile *.spec 0r /usr/share/vim/vimfiles/template.spec
  augroup END
endif

if has("cscope") && filereadable("/usr/bin/cscope")
   set csprg=/usr/bin/cscope
   set csto=0
   set cst
   set nocsverb
   " add any database in current directory
   if filereadable("cscope.out")
      cs add $PWD/cscope.out
   " else add database pointed to by environment
   elseif $CSCOPE_DB != ""
      cs add $CSCOPE_DB
   endif
   set csverb
endif

" Switch syntax highlighting on, when the terminal has colors
" Also switch on highlighting the last used search pattern.
if &t_Co > 2 || has("gui_running")
  syntax on
endif


filetype off
set rtp+=/root/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'jiangmiao/auto-pairs'
Plugin 'Yggdroot/indentLine'
Plugin 'vim-syntastic/syntastic'
Plugin 'rkulla/pydiction'
Plugin 'scrooloose/nerdtree'
Plugin 'majutsushi/tagbar'
call vundle#end()
filetype plugin indent on

syntax on
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab
set nu

set nobackup
set noswapfile
set nowritebackup

set ignorecase
set smartcase

map <Enter> o<ESC>
map <S-Enter> O<ESC>

"tagbar
nmap <Leader>tb :TagbarToggle<CR>
let g:tagbar_ctags_bin='/bin/ctags'
let g:tagbar_width=30
map <F3> :Tagbar<CR>


"map <C-F12> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR>

autocmd filetype python nnoremap <F5> :w! <bar> exec '!python '.shellescape('%')<CR>


let g:ycm_global_ycm_extra_conf='/root/.ycm_extra_conf.py'
let g:ycm_seed_identifiers_with_syntax=1
let g:ycm_confirm_extra_conf=0
let g:ycm_key_invoke_completion = '<C-a>'
set completeopt=longest,menu
let g:ycm_path_to_python_interpreter='/usr/bin/python3.6'
let g:ycm_complete_in_strings = 1


" Plugin syntastic settings.
set statusline+=%#waringmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0
let g:syntastic_mode_map = {'mode': 'passive', 'active_filetypes': [], 'passive_filetypes': []}
" Use pylint to check python files
let g:syntastic_python_checkers = ['pylint']
map <F4> :SyntasticToggleMode<CR> :SyntasticCheck<CR>


"Ignore warnings about newlines trailing.
let g:syntastic_quiet_messages = { 'regex': ['trailing-newlines', 'invalid-name',
    \'too-many-lines', 'too-many-instance-attributes', 'too-many-public-methods',
    \'too-many-locals', 'too-many-branches'] }


let g:pydiction_location = '/root/.vim/bundle/pydiction/complete-dict'
let g:pydiction_menu_height = 9




" indent line
let g:indentLine_char = "|"
let g:indentLine_enabled = 1
let g:autopep8_disable_show_diff=1



function HeaderPython()
    call setline(1, "#!/usr/bin/env python")
    call setline(2, "# -*- coding: utf-8 -*-")
    call setline(3, "# author: otfsenter")
    normal G
    normal o
endf

autocmd bufnewfile *.py call HeaderPython()






