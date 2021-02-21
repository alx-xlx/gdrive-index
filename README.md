
<div align="center">
<img src="https://i.imgur.com/XYChjKr.png" alt="gdrive-index" height="">
gdrive-index
</div>
 <div align="center">
 <img alt="gdrive-index-license" src="https://img.shields.io/badge/Open_source-MIT-red.svg?logo=git&logoColor=green"/>
<img src="https://img.shields.io/github/last-commit/alx-xlx/gdrive-index.svg?logo=Sublime+Text&logoColor=green&label=Active"/>
<img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/alx-xlx/gdrive-index">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/alx-xlx/gdrive-index">
<img alt="gdrive-index-softwareheritage.org" src="https://archive.softwareheritage.org/badge/origin/https://github.com/Unipisa/CMM/"/>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/alx-xlx/gdrive-index">
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Falx-xlx%2Fgdrive-index&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Views&edge_flat=false"/>

</div>
 
# GDrive-Index

It is a multiplatform CLI-only clone of [Snap2HTML](http://www.rlvision.com/snap2html/about.php).
I created it because I needed to use Snap2HTML on Linux but didn't want to have to install WINE. Also because I wanted to make it possible to use it on a headless machine, so that's why there is no GUI 

It's purpose is to create single page HTML+ Javascript browsable lists of the contents of a given directory

[**example.html**](https://alx-xlx.github.io/gdrive-index/example.html) - https://alx-xlx.github.io/gdrive-index/example.html

**example.png**

![](example.png)

## Usage
### 1. Run this Colab Script to Index Google Drive
<!-- Open in Colab in Center -->
<a href="https://colab.research.google.com/github/alx-xlx/gdrive-index/blob/master/gdrive_index.ipynb" rel="nofollow"><img src="https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" class='centre' data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg" style="max-width:100%;display:block;margin-left:auto;margin-right:auto;"></a>

<!-- https://i.imgur.com/hCFNHhN.gif -->

<!-- ![](https://i.imgur.com/sj4PEUo.gif) -->

<p align="center"><img src="https://i.imgur.com/sj4PEUo.gif" alt="LOGO"></p>

OR

### 2. Run Locally to Index Local Drives

The program only takes two arguments, the directory to be indexed and the output file name without the extension, so:

```gdrive-index.py /home/user filelist```
 
Will index the contents of /home/user and save them to filelist.html on the current directory. Simple as that


## License
The gdrive-index.py file is licensed under GPLv2

The template.html file is taken directly from Snap2HTML an thus is licensed as freeware
