init -1 python:
    def preloadImages(dlQueue):
        show_loading()
        #renpy.pause()

        enqueued = []

        for i in dlQueue:
            try:
                if ".ogg" in i:
                    renpy.loader.load("audio/" + i)
                else:
                    renpy.loader.load("images/" + i)
            
            except renpy.webloader.DownloadNeeded as e:
                if ".ogg" in i:
                    renpy.webloader.enqueue(e.relpath, 'music', "audio/" + i)
                else:
                    renpy.webloader.enqueue(e.relpath, 'image', "images/" + i)
                enqueued.append(e.relpath)
                #renpy.notify("Enqueueing %s" % e.relpath)
        
        while 1:
            if not enqueued:
                hide_loading()
                return
            for x in enqueued:
                fullpath = os.path.join(renpy.config.gamedir, x)
                if not os.path.exists(fullpath): # be patient
                    continue
                else:
                    enqueued.remove(x)
            renpy.pause(0.1, hard=True)
        hide_loading()