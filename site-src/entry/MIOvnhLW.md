---
title: '[译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？'
sidebar: false
---

::: info
[← 返回基础设施](/infra)
:::

# [译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？

> Cubox 收藏 — [译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=MzI4MTQyNzkxNw==&mid=2247484077&idx=1&sn=a9ea8f707fe733c43f8c5e8b119efd95&chksm=eaa3bb549d34d9b69fa713d6f5a05ee7aebbe587ddbcc7105cdfb25ececa5bd138a5a140cde0&mpshare=1&scene=1&srcid=0406EAJwfSBv8kNBXXR6T3mD&sharer_shareinfo=1285f5c35b21a56bde53198b6074ed60&sharer_shareinfo_first=1285f5c35b21a56bde53198b6074ed60) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2025-04-06

---

# [译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？

## English
<!DOCTYPE html>
`html`>
	`head`>
		`meta` http-equiv="content-type" content="text/html;charset=utf8">
		`meta` id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />
		`title`>未知错误`title`>
		`style`>	
			html,body{
				height:100%;
				padding:0px;
				margin:0px;
			}
			body{
				background-color: #F4F4F4;
			}
			.panel {
				padding: 18px 22px 10px;	
			}
			.mesg-block{
				margin-bottom:20px;
			}
			.mesg-block p{
				font-size: 16px;
				line-height: 1.3em;
				color: #858585;
				text-shadow: 0px 1px 0px #FFF;
				text-align:center;
			}
		`style`>
	`head`>
	`body`>
		`div` class="panel">
			`div` class="mesg-block">
				`p`>未知错误，请稍后再试`p`>
			`div`>	
		`div`>
		`script`  nonce="" reportloaderror>
			(function(){
			 	
				document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
					var appId = '',
						imgUrl = ''
						link = 'http://mp.weixin.qq.com/mp/conference/default/share',
						title = '失效的验证页面'
						desc = '你暂无权限查看此页面内容。',
						content = '#微信分享#，你暂无权限查看此页面内容。';
					
					
					WeixinJSBridge.on('menu:share:appmessage', function(argv){
						WeixinJSBridge.invoke('sendAppMessage',{
											  "appid":appId,
											  "img_url":imgUrl,
											  "img_width":"640",
											  "img_height":"640",
											  "link":link,
											  "desc":desc,
											  "title":title
											  }, function(res) {})
					});
					
					WeixinJSBridge.on('menu:share:timeline', function(argv){
						WeixinJSBridge.invoke('shareTimeline',{
											  "img_url":imgUrl,
											  "img_width":"640",
											  "img_height":"640",
											  "link":link,
											  "desc": desc,
											  "title":title
											  }, function(res) {
											  });
					});

					
					var weiboContent = '';
					WeixinJSBridge.on('menu:share:weibo', function(argv){
						WeixinJSBridge.invoke('shareWeibo',{
											  "content":content,
											  "url":link,
											  }, function(res) {
											  });
					});
					
					WeixinJSBridge.call('hideOptionMenu');
				}, false);
			})();
		`script`>
		`body`>
	`head`>
`html`>


## 中文
[待翻译的英文内容]
