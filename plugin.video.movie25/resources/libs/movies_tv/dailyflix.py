import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/art', ''))

    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def LISTSP3(murl):
        if murl == 'HD':
                url='http://www.dailyflix.net/index.php?/forum/196-hd-movies-2012-2013/page__sort_key__last_post__sort_by__Z-A'
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('&#38;','&')
        match=re.compile('<a itemprop=".+?" id=".+?" href="([^<]+)" title=.+? class=.+?><span itemprop="name">(.+?)</span>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url, name in match:
                name=main.unescapes(name)
                main.addPlayM(name,url,54,'','','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("HD-TV","Dailyfix")
        main.VIEWS()


def LINKSP3(mname,url):
        main.GA("Dailyfix","Watched")
        sources = []
        ok=True
        infoLabels =main.GETMETAT(mname,'','','')
        video_type='movie'
        season=''
        episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,3000)")
        link=main.OPENURL(url)
        match=re.compile("<a href='(.+?)' class='.+?' title='.+?' rel='.+?'>.+?</a").findall(link)
        for murl in match:
                host=re.compile("http://(.+?).com/.+?").findall(murl)
                for hname in host:
                        hname=hname.replace('www.','')
                        hosted_media = urlresolver.HostedMediaFile(url=murl, title=hname)
                        sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Movie doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
        try:
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Actual HD Movie Requires Buffer Time,7000)")
                        stream_url = source.resolve()
                else:
                        stream_url = False
                        return
                infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
                # play with bookmark
                player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
                #WatchHistory
                if selfAddon.getSetting("whistory") == "true":
                    wh.add_item(mname+' '+'[COLOR green]DailyFix[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=img, fanart=fanart, is_folder=False)
                player.KeepAlive()
                return ok
        except:
                return ok
        
