from changer import AmbientBackgrounds

class Main:
    def run(self):
        self.ambient_bg = AmbientBackgrounds()
        self.ambient_bg.begin()

if __name__ == "__main__":
    Main().run()
