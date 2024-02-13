"""
A module for downloading media from given URLs using yt-dlp.

This module provides a class, MediaDownloader, that encapsulates functionality for downloading 
media from URLs using yt-dlp library.

Classes:
    MediaDownloader: A class for downloading media from given URLs using yt-dlp.

Attributes:
    SUGGESTIONS (dict): A dictionary containing suggestions for download settings.
"""

from os import path
from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError


class MediaDownloader:
    """
    A class for downloading media from given URLs using yt-dlp.

    Attributes:
        urls (list): A list of URLs to download media from.
        settings (dict): A dictionary containing download settings such as format, outtmpl,
        and postprocessors.
    """

    def __init__(self) -> None:
        """
        Initializes the MediaDownloader with default settings.
        """
        self.urls = []
        self.settings = {
            "format": "best",
            "outtmpl": self.get_user_downloads_path() + "/%(title)s.%(ext)s",
            "postprocessors": [],
        }

    def get_user_downloads_path(self) -> str:
        """
        Returns the default download path.
        """
        return path.expanduser("~/Downloads")

    def _get_media_dl(self) -> YoutubeDL:
        """
        Returns an instance of YoutubeDL configured with the current settings.
        """
        return YoutubeDL(self.settings)

    def set_media_settings(
        self,
        new_format: str | None = None,
        new_outtmpl: str | None = None,
        new_postprocessors: list | None = None,
    ) -> None:
        """
        Sets the download settings.

        Args:
            new_format (str): The format to use for downloading media.
            new_outtmpl (str): The output template for downloaded media files.
            new_postprocessors (list): A list of postprocessors to apply after downloading.
        """
        if new_format:
            self.settings["format"] = new_format

        if new_outtmpl:
            self.settings["outtmpl"] = new_outtmpl

        if new_postprocessors:
            self.settings["postprocessors"] = new_postprocessors

    def set_urls(self, new_url_list: list) -> None:
        """
        Sets the URLs to download media from.

        Args:
            new_url_list (list): A list of URLs to download media from.
        """
        self.urls = new_url_list

    def download_media(self) -> None:
        """
        Downloads media from the specified URLs using the current settings.
        """
        self._get_media_dl().download(self.urls)

    def get_info(self, url: str) -> dict:
        """
        Returns information about the media being downloaded.
        """
        ydl_opts = {
            'quiet': True,
            'simulate': True,  # No descarga el video, solo simula la descarga y muestra información
            'dump_single_json': True,  # Dump output to single json format
        }

        with YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                return {
                'title': info.get('title', 'N/A'),
                'duration': info.get('duration', 'N/A'),
                'thumbnail': info.get('thumbnail', 'N/A')
                }
            except YoutubeDLError as e:
                print(f"Error al obtener información: {str(e)}")


SUGGESTIONS = {
    "formats": (
        "best",
        "worst",
        "bestvideo[height=quality_video]+bestaudio[abr=quality_audio]/best",
    ),
    "qualities": {
        "video": [144, 240, 360, 480, 720, 1080, 1440, 2160],
        "audio": [48, 96, 128, 192, 256, 320],
    },
    "outtmpl_extensions": {
        "video": ["mp4", "mkv", "webm", "avi", "mov", "flv"],
        "audio": ["mp3", "wav", "ogg", "m4a", "3gp"],
    },
    "postprocessors": {
        "audio_extract_mp3": {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
            "nopostoverwrites": True,
        },
        "audio_convert_mp3": {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp3",
            "nopostoverwrites": True,
        },
        "video_convert_mp4": {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
            "nopostoverwrites": True,
        },
        "merger": {"key": "FFmpegMerger", "preferedformat": "mp4"},
    },
}
