import media

class MediaServiceSingleton:

    instance = None

    @staticmethod
    def get_instance():
        if MediaServiceSingleton.instance is None:
            MediaServiceSingleton.instance = MediaServiceSingleton()
        return MediaServiceSingleton.instance


