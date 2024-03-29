1. 项目需求：在日常使用壁纸网站时，由于加载速度慢和批量下载困难，用户往往难以快速找到并使用自己喜欢的壁纸。为了解决这个问题，该项目旨在通过批量下载壁纸到本地文件夹，使用户能够更方便地挑选和使用壁纸。
2. 项目描述：本项目利用Python的requests、pool、re和os等第三方库，实现了对网页上壁纸信息的批量爬取和下载。具体流程如下：
    · 首先，使用requests库获取网页的源代码。这为后续的壁纸链接获取提供了基础。
    · 其次，通过在浏览器中打开开发者工具（F12），查看网页源码，并利用正则表达式（re库）批量获取每个壁纸的URL链接。这一步是整个项目中最为关键的一环，因为它直接决定了能够下载到哪些壁纸。
    · 然后，使用os库创建一个新的文件夹，用于存储获取到的URL链接。这一步为后续的下载工作做好了准备。
    · 最后，利用pool库中的进程池方法，优化了下载壁纸的速度。这样，用户可以更快地获取到自己需要的壁纸。
通过以上步骤，本项目成功地解决了用户在壁纸网站上选择壁纸时遇到的问题，大大提高了用户的使用体验。

由于该网址在国内被封，目前只能使用魔法可以运行
