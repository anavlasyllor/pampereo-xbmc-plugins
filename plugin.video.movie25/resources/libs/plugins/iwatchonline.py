import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net
net = Net()
from resources.libs import main

#Mash Up - by Mash2k3 2012.

from t0mm0.common.addon import Addon
from universal import playbackengine, watchhistory
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon('plugin.video.movie25', sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/art', ''))

    
wh = watchhistory.WatchHistory('plugin.video.movie25')

def AtoZiWATCHtv():
    main.addDir('0-9','http://www.iwatchonline.to/main/content_more/tv/?startwith=09&start=0',589,art+'/wfs/09.png')
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.iwatchonline.to/main/content_more/tv/?startwith='+i.lower()+'&start=0',589,art+'/wfs/'+i+'.png')
    main.GA("Tvshows","A-ZTV")
    main.VIEWSB()

def AtoZiWATCHm():
    main.addDir('0-9','http://www.iwatchonline.to/main/content_more/movies/?startwith=09&start=0',587,art+'/wfs/09.png')
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.iwatchonline.to/main/content_more/movies/?startwith='+i.lower()+'&start=0',587,art+'/wfs/'+i+'.png')
    main.GA("Movies","A-ZM")
    main.VIEWSB()

def iWatchMAIN():
        main.addDir('Movies','http://www.iwatchonline.org/',586,art+'/wfs/iwatchm.png')
        main.addDir('Tv Shows','http://www.iwatchonline.org/',585,art+'/wfs/iwatcht.png')
        main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,art+'/wfs/iwatcht.png')
        main.GA("Plugin","iWatchonline")
        main.VIEWSB2()

        
def iWatchMOVIES():
        main.addDir('Search','http://www.iwatchonline.to',644,art+'/wfs/searchws.png')
        main.addDir('A-Z','http://www.iwatchonline.to',595,art+'/wfs/azws.png')
        main.addDir('Popular','http://www.iwatchonline.to/main/content_more/movies/?sort=popular&start=0',587,art+'/wfs/iwatchm.png')
        main.addDir( 'Latest Added','http://www.iwatchonline.to/main/content_more/movies/?sort=latest&start=0',587,art+'/wfs/iwatchm.png')
        main.addDir('Featured Movies','http://www.iwatchonline.to/main/content_more/movies/?sort=featured&start=0',587,art+'/wfs/iwatchm.png')
        main.addDir('Latest HD Movies','http://www.iwatchonline.to/main/content_more/movies/?quality=hd&start=0',587,art+'/wfs/iwatchm.png')
        main.addDir( 'Upcoming','http://www.iwatchonline.to/main/content_more/movies/?sort=upcoming&start=0',587,art+'/wfs/iwatchm.png')
        main.addDir('Genre','http://www.iwatchonline.to',596,art+'/wfs/genrews.png')
        main.GA("iWatchonline","Movies")
        main.VIEWSB2()

def iWatchTV():
        main.addDir('Search','http://www.iwatchonline.to',642,art+'/wfs/searchws.png')
        main.addDir('A-Z','http://www.iwatchonline.to',593,art+'/wfs/azws.png')
        main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,art+'/wfs/iwatcht.png')
        main.addDir('Featured Shows','http://www.iwatchonline.to/main/content_more/tv/?sort=featured&start=0',589,art+'/wfs/iwatcht.png')
        main.addDir('Popular Shows','http://www.iwatchonline.to/main/content_more/tv/?sort=popular&start=0',589,art+'/wfs/iwatcht.png')
        main.addDir('Latest Additions','http://www.iwatchonline.to/main/content_more/tv/?sort=latest&start=0',589,art+'/wfs/iwatcht.png')
        main.addDir('Genre','http://www.iwatchonline.to',594,art+'/wfs/genrews.png')
        main.GA("iWatchonline","Tvshows")
        main.VIEWSB2()

def SearchhistoryTV():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='ws'
            SEARCHTV(url)
        else:
            main.addDir('Search','ws',643,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,643,thumb)
            
            


def SEARCHTV(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'ws':
            keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    if not os.path.exists(SeaFile) and encode != '':
                        open(SeaFile,'w').write('search="%s",'%encode)
                    else:
                        if encode != '':
                            open(SeaFile,'a').write('search="%s",'%encode)
                    searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                    for seahis in reversed(searchis):
                        continue
                    if len(searchis)>=10:
                        searchis.remove(searchis[0])
                        os.remove(SeaFile)
                        for seahis in searchis:
                            try:
                                open(SeaFile,'a').write('search="%s",'%seahis)
                            except:
                                pass


        else:
            encode = murl
        search_url = 'http://www.iwatchonline.to/search'
        search_content = net.http_POST(search_url, { 'searchquery' : encode, 'searchin' : 't'} ).content
        r = re.findall('(?s)<table(.+?)</table>',search_content)
        r=main.unescapes(r[0])
        match=re.compile('<img.+?src=\"(.+?)\".+?<a.+?href=\"(.+?)\">(.+?)</a>').findall(r)
        for thumb,url,name in match:
                main.addDirT(name,url,590,thumb,'','','','','')
        main.GA("iWatchonline","Search")


def SearchhistoryM():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='ws'
            SEARCHM(url)
        else:
            main.addDir('Search','ws',645,art+'/search.png')
            main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
            thumb=art+'/link.png'
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,645,thumb)
            
            


def SEARCHM(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'ws':
            keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    if not os.path.exists(SeaFile) and encode != '':
                        open(SeaFile,'w').write('search="%s",'%encode)
                    else:
                        if encode != '':
                            open(SeaFile,'a').write('search="%s",'%encode)
                    searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                    for seahis in reversed(searchis):
                        continue
                    if len(searchis)>=10:
                        searchis.remove(searchis[0])
                        os.remove(SeaFile)
                        for seahis in searchis:
                            try:
                                open(SeaFile,'a').write('search="%s",'%seahis)
                            except:
                                pass


        else:
            encode = murl
        search_url = 'http://www.iwatchonline.to/search'
        search_content = net.http_POST(search_url, { 'searchquery' : encode, 'searchin' : 'm'} ).content
        r = re.findall('(?s)<table(.+?)</table>',search_content)
        r=main.unescapes(r[0])
        match=re.compile('<img.+?src=\"(.+?)\".+?<a.+?href=\"(.+?)\">(.+?)</a>').findall(r)
        for thumb,url,name in match:
                main.addPlayM(name,url,588,thumb,'','','','','')
        main.GA("iWatchonline","Search")
        
def iWatchGenreTV():
        link=main.OPENURL('http://www.iwatchonline.to/tv-show')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<li>  <a href=".?gener=([^<]+)">  (.+?)  </a>  </li>').findall(link)
        for url,genre in match:
                main.addDir(genre,'http://www.iwatchonline.to/main/content_more/tv/?gener='+url+'&start=0',589,'')
        main.GA("Tvshows","GenreT")
def iWatchGenreM():
        link=main.OPENURL('http://www.iwatchonline.to/movies')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<li>  <a href=".?gener=([^<]+)">  (.+?)  </a>  </li>').findall(link)
        for url,genre in match:
                main.addDir(genre,'http://www.iwatchonline.to/main/content_more/movies/?gener='+url+'&start=0',587,'')
        main.GA("Movies","GenreM")                

def iWatchLISTMOVIES(murl):
        main.GA("Movies","List")   
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="(.+?)" class=".+?" rel=".+?"><img class=".+?" src="(.+?)" alt=""> <div class=".+?">.+?</div>  </a><div class=".+?">(.+?)<div class=".+?"><div class=".+?" data-rating=".+?"></div></div></div><div class=".+?">(.+?)<br />').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,desc in match:    
                main.addDirM(name,url,588,thumb,desc,'','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        if len(match)==25:
            paginate=re.compile('([^<]+)start=([^<]+)').findall(murl)
            for purl,page in paginate:
                i=int(page)+25
                main.addDir('[COLOR blue]Next[/COLOR]',purl+'start='+str(i),587,art+'/next2.png')
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def iWatchToday(murl):
        main.GA("Tvshows","TodaysList")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<img src="([^<]+)" alt="" class=".+?"><br /><a href="(.+?)">(.+?)</a>  </td>  <td style=".+?" width=".+?">(.+?)</td>  <td style=".+?" width=".+?">(.+?)</td>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for thumb,url,name,episea,epiname in match:
                name=name.replace('(','').replace(')','')
                name=name.replace('(\d{4})','')
                main.addDirTE(name+' '+episea+' '+epiname,url,588,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait

def iWatchLISTSHOWS(murl):
        main.GA("Tvshows","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="(.+?)" class=".+?" rel=".+?"><img class=".+?" src="(.+?)" alt=""> <div class=".+?">.+?</div>  </a><div class=".+?">(.+?)<div class=".+?"><div class=".+?" data-rating=".+?"></div></div></div><div class=".+?">(.+?)<br />').findall(link)
        for url,thumb,name,desc in match:
                main.addDirT(name,url,590,thumb,desc,'','','','')
        print len(match)
        if len(match)==25:
            paginate=re.compile('([^<]+)start=([^<]+)').findall(murl)
            for purl,page in paginate:
                i=int(page)+25
                main.addDir('[COLOR blue]Next[/COLOR]',purl+'start='+str(i),589,art+'/next2.png')
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def iWatchSeason(name,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<meta name="description" content="(.+?)">').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<div class="movie-cover span2"><img src="(.+?)" alt=".+?" class=".+?" />').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match=re.compile('<h5><i class=".+?"></i>  (.+?)</h5>').findall(link)
        for season in match:
                main.addDir2(name+' '+season,murl,591,thumb,desc)

def iWatchEpisode(mname,murl):
        seanum  = mname.split('n ')[1]
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<meta name="description" content="(.+?)">').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<div class="movie-cover span2"><img src="(.+?)" alt=".+?" class=".+?" />').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match=re.compile('<td class="sideleft"><a href="([^<]+)"><i class="icon-play-circle"></i>(.+?)</a></td>  <td>(.+?)</td>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Episodes loading...'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for url,epi,name in match:
                mname=mname.replace('(','').replace(')','')
                mname = re.sub(" \d{4}", "", mname)
                sea=re.compile('s'+str(seanum)).findall(url)
                if len(sea)>0:
                        main.addDirTE(mname+epi+'   '+name,url,588,thumb,desc,'','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Episodes loading...'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('episodes-view'))

def GetUrl(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('class="frame" src="(.+?)"').findall(link)
        link=match[0]
        return link

def iWatchLINK(mname,url):      
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,1500)")
        link=main.OPENURL(url)
        link=main.unescapes(link)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        match=re.compile('<td class="sideleft"><a href="([^<]+)" target=".+?" rel=".+?"><img src=".+?" alt="" />(.+?)</a>').findall(link)
        for url, name in match:
            name=name.replace(' ','')
            if name[0:1]=='.':
                name=name[1:]
            name=name.split('.')[0]
            main.addDown2(mname+' [COLOR red]'+name.upper()+'[/COLOR]',url,649,art+'/hosts/'+name.lower()+'.png',art+'/hosts/'+name.lower()+'.png')


def iWatchLINKB(mname,url):
        main.GA("iWatchonline","Watched")
        ok=True
        hname=mname
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        mname=mname.split('   [COLOR red]')[0]
        r=re.findall('Season(.+?)Episode([^<]+)',mname)
        if r:
            infoLabels =main.GETMETAEpiT(mname,'','')
            video_type='episode'
            season=infoLabels['season']
            episode=infoLabels['episode']
        else:
            infoLabels =main.GETMETAT(mname,'','','')
            video_type='movie'
            season=''
            episode=''
        img=infoLabels['cover_url']
        fanart =infoLabels['backdrop_url']
        imdb_id=infoLabels['imdb_id']
        infolabels = { 'supports_meta' : 'true', 'video_type':video_type, 'name':str(infoLabels['title']), 'imdb_id':str(infoLabels['imdb_id']), 'season':str(season), 'episode':str(episode), 'year':str(infoLabels['year']) }
        link=main.OPENURL(url)
        link=main.unescapes(link)
        match=re.compile('<iframe.+?src=\"(.+?)\"').findall(link)
        hosted_media = urlresolver.HostedMediaFile(match[0])
        source=hosted_media
        try :
            if source:
                    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                    stream_url = source.resolve()
            else:
                    stream_url = False
                    return
                
            infoL={'Title': infoLabels['title'], 'Plot': infoLabels['plot'], 'Genre': infoLabels['genre']}
            # play with bookmark
            player = playbackengine.PlayWithoutQueueSupport(resolved_url=stream_url, addon_id=addon_id, video_type=video_type, title=str(infoLabels['title']),season=str(season), episode=str(episode), year=str(infoLabels['year']),img=img,infolabels=infoL, watchedCallbackwithParams=main.WatchedCallbackwithParams,imdb_id=imdb_id)
            #WatchHistory
            if selfAddon.getSetting("whistory") == "true":
                wh.add_item(hname+' '+'[COLOR green]iWatchonline[/COLOR]', sys.argv[0]+sys.argv[2], infolabels=infolabels, img=str(img), fanart=str(fanart), is_folder=False)
            player.KeepAlive()
            return ok
        except:
            return ok
            

