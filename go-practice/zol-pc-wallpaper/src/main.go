package main

import (
	"bytes"
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"golang.org/x/text/encoding/simplifiedchinese"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
	"sync"
	"time"
)

var zolHomeSite string
var imageDirectory string

func init() {
	zolHomeSite = "http://desk.zol.com.cn"
	imageDirectory = "D:\\zol-pc-images\\"
}

func DecodeToGBK(text string) (ret string, err error) {
	dst := make([]byte, len(text)*2)
	tr := simplifiedchinese.GB18030.NewDecoder()
	nDst, _, err := tr.Transform(dst, []byte(text), true)
	if err != nil {
		return text, err
	}
	return string(dst[:nDst]), nil
}

type CategoryInfo struct {
	link string
	name string
}

type AlbumInfo struct {
	link string
	name string
}

func PathExists(path string) bool {
	_, err := os.Stat(path)
	if err == nil {
		return true
	}
	if os.IsNotExist(err) {
		return false
	}
	return false
}

func getCategories() (categoryList []CategoryInfo) {
	doc, _ := goquery.NewDocument(zolHomeSite + "/pc/")
	doc.Find(".choosebox > .filter-item").First().Find(".brand-sel-box > a").Each(func(i int, s *goquery.Selection) {
		content, _ := s.Html()
		link, _ := s.Attr("href")
		content2, _ := DecodeToGBK(content)
		if "" != link {
			categoryList = append(categoryList, CategoryInfo{link: link, name: content2})
		}
	})
	return categoryList
}

func getSubCategories(category CategoryInfo) (subCategoryList []CategoryInfo) {
	doc, _ := goquery.NewDocument(zolHomeSite + category.link)
	doc.Find(".choosebox > .filter-item").Next().First().Find(".brand-sel-box > a").Each(func(i int, s *goquery.Selection) {
		content, _ := s.Html()
		link, _ := s.Attr("href")
		content2, _ := DecodeToGBK(content)
		if "" != link {
			subCategoryList = append(subCategoryList, CategoryInfo{
				link: link,
				name: content2,
			})
		}
	})
	return subCategoryList
}

func getWallpaperAlbumList(pageLink string) (albumList []AlbumInfo, nextLink string) {
	doc, _ := goquery.NewDocument(zolHomeSite + pageLink)
	doc.Find(".pic-list2").First().Find(".photo-list-padding").Each(func(i int, s *goquery.Selection) {
		albumName, _ := s.Find("a > span").Attr("title")
		albumName, _ = DecodeToGBK(albumName)
		albumLink, _ := s.Find("a").Attr("href")
		println(albumName, albumLink)
		albumList = append(albumList, AlbumInfo{
			link: albumLink,
			name: albumName,
		})
	})
	nextLink1, exists := doc.Find("#pageNext").Attr("href")
	print(nextLink1, exists)
	nextLink = nextLink1
	if exists == false {
		nextLink = ""
	}
	return albumList, nextLink
}

func downloadImage(category CategoryInfo, subCategory CategoryInfo, album AlbumInfo, picLink string) (imageFileName string) {
	strs := strings.Split(picLink, "/")
	imageFileName = strs[len(strs)-1]
	resp, _ := http.Get(picLink)
	body, _ := ioutil.ReadAll(resp.Body)
	out, _ := os.Create(imageDirectory + category.name + "\\" + subCategory.name + "\\" + album.name + "\\" + imageFileName)
	_, _ = io.Copy(out, bytes.NewReader(body))
	return imageFileName
}

func saveImage(category CategoryInfo, subCategory CategoryInfo, album AlbumInfo, imageLink string) {
	doc, _ := goquery.NewDocument(zolHomeSite + imageLink)
	link, _ := doc.Find("#tagfbl > a").First().Attr("href")
	if !strings.Contains(link, "http://") {
		println("link", zolHomeSite+imageLink, link)
		showPicDoc, err := goquery.NewDocument(zolHomeSite + link)
		if err != nil {
			return
		}
		picLink, exists := showPicDoc.Find("img").First().Attr("src")
		if exists == false {
			return
		}
		downloadImage(category, subCategory, album, picLink)
	}
}

func saveAlbum(category CategoryInfo, subCategory CategoryInfo, album AlbumInfo) {
	var wg sync.WaitGroup
	doc, _ := goquery.NewDocument(zolHomeSite + album.link)
	doc.Find("#showImg > li").Each(func(i int, selection *goquery.Selection) {
		imageLink, _ := selection.Find("a").Attr("href")
		wg.Add(1)
		go func(category CategoryInfo, subCategory CategoryInfo, album AlbumInfo, imageLink string) {
			saveImage(category, subCategory, album, imageLink)
			wg.Done()
		}(category, subCategory, album, imageLink)
	})
	wg.Wait()
}

func main() {
	startTime := time.Now().UnixNano()
	var wg sync.WaitGroup
	categoryList := getCategories()
	//获取壁纸分类
	for _, category := range categoryList {
		println(category.link, category.name)
		if !PathExists(imageDirectory + category.name) {
			_ = os.Mkdir(imageDirectory+category.name, os.ModePerm)
		}
		//获取壁纸子类
		wg.Add(1)
		go func(category CategoryInfo) {
			for _, subCategory := range getSubCategories(category) {
				if !PathExists(imageDirectory + category.name + "\\" + subCategory.name) {
					_ = os.Mkdir(imageDirectory+category.name+"\\"+subCategory.name, os.ModePerm)
				}
				println(category.link, category.name, "=>", subCategory.link, subCategory.name)
				nextLink := subCategory.link
				//获取壁纸列表
				for nextLink != "" {
					var albumList []AlbumInfo
					albumList, nextLink = getWallpaperAlbumList(nextLink)
					for _, album := range albumList {
						if !PathExists(imageDirectory + category.name + "\\" + subCategory.name + "\\" + album.name) {
							_ = os.Mkdir(imageDirectory+category.name+"\\"+subCategory.name+"\\"+album.name, os.ModePerm)
						}
						println(album.name, album.link)
						saveAlbum(category, subCategory, album)
					}
				}
			}
			wg.Done()
		}(category)
	}
	wg.Wait()
	fmt.Printf("\n%.2fs\n", float64(time.Now().UnixNano()-startTime)/1000000000.0)
}
