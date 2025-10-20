import matplotlib as plt

class DrawModule:
    def __init__(self):
        """Setting default values"""
        self.dpi = 100;
        self.color_map = 'magma'
        self.destination = './'
        self.ready = False
        
    def set_dpi(self, dpi):
        self.dpi = dpi
    
    def set_color_map(self, color_map):
        self.color_map = color_map
    
    def save_to_file(self, filename):
        if not self.ready:
            raise Exception("Failied to show plot: plot is not prepared yet")
        path = f"{self.destination}/{filename}.png"
        plt.savefig(path, dpi=self.dpi, bbox_inches='tight');
        
    def show_plot(self):
        if not self.ready:
            raise Exception("Failied to show plot: plot is not prepared yet")
        plt.show();
        
    def generate_plot(self, image_data, extent, title, colorbar_title):
        plt.imshow(image_data, cmap=self.color_map, extent=extent)
        plt.xlabel("Re(c)")
        plt.ylabel("Im(c)")
        plt.title(title)
        plt.colorbar(colorbar_title)
        self.ready = True;
        
    def clean_up(self):
        plt.close()
        self.ready = False