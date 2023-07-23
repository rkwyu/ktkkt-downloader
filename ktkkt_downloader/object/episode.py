class Episode():
    def __init__(self, id:str, name:str, episode_no:str, url:str, m3u8:str) -> None:
        self.id = id
        self.name = name
        self.episode_no = episode_no
        self.url = url
        self.m3u8 = m3u8