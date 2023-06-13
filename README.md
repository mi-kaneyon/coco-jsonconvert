# coco-jsonconvert
coco format exported by label studio utility

<p align="center">
  <img src="https://github.com/mi-kaneyon/coco-jsonconvert/blob/main/git-converter.png" height="450"  title="hover text">
</p>

## necessary module
scikit-learn
```
pip install scikit-learn

```

## function
- remove prefix from image file which is generated by label studio
- partition out train and val around ideal percentage
- create modified json file for each directory

```

result.json  #---include label studio compress file(whole image annotation data)
├── images  #---coco data compress file from label studio
├── train  #---please create yourself(output file directory)
└── val     #---please create yourself(output file directory)  

```


## command line
```
 python sec_labeconv.py 

```
# Reference
- label studio

https://github.com/heartexlabs/label-studio

