import numpy as np
import matplotlib.pyplot as plt

class Core():
    """Main class represents evaluating model"""
    def __init__(self, xmin, xmax, width, ymin, ymax, height):
        self.xmin = xmin
        self.xmax = xmax
        self.width = width
        self.ymax = ymax
        self.ymin = ymin
        self.height = height
        self.max_iter = 0
        self.prepared = False
    
    def set_max_iter(self, value):
        self.max_iter = value
        
    def run(self, max_iter=200):
        """Prepare&process data for rendering"""
        self.set_max_iter(max_iter)
        x = np.linspace(self.xmin, self.xmax, self.width) 
        y = np.linspace(self.ymax, self.ymin, self.height)
        X, Y = np.meshgrid(x, y) # X&Y axes of square plane area 
        C = X + 1j * Y # complex plane area
        Z = np.zeros(C.shape, dtype=np.complex128) # for sequens values
        N = np.zeros(C.shape, dtype=np.int32) # for iteration depth control
        for i in range(max_iter):
            mask_not_escaped = np.abs(Z) <= 2.0
            if not np.any(mask_not_escaped):
                break
            Z[mask_not_escaped] = Z[mask_not_escaped]**2 + C[mask_not_escaped]
            mask_escaped_now = (mask_not_escaped) & (np.abs(Z) > 2.0)
            N[mask_escaped_now] = i + 1
            
        self.__prepare_plot(N, Core.__colorize(N, Z, self.max_iter))
        
    def __prepare_plot(self, N, nu):
        final_image_data = np.zeros(N.shape, dtype=float)
        final_image_data[N > 0] = nu
        plt.imshow(final_image_data, cmap='hot', extent=[self.xmin, self.xmax, self.ymin, self.ymax])
        plt.xlabel("Re(c)")
        plt.ylabel("Im(c)")
        plt.title(f"Mandelbrot Set ({self.width}x{self.height}, {self.max_iter} iter)")
        plt.colorbar(label="Iterations to Escape(normalized)")
        self.prepared = True
        
    def __colorize(N, Z, max_iter):
        """Used to make color smoothing"""
        mask_escaped = N > 0 
        N_escaped = N[mask_escaped]
        Z_escaped = Z[mask_escaped]
        
        log_Z_escaped = np.log(np.log(np.abs(Z_escaped))) / np.log(2)
        nu = N_escaped + 1 - log_Z_escaped
        nu_normalized = np.log(nu) / np.log(max_iter);
        return nu_normalized
        
        
    def save_plot(self, destination='./mandelbrot/render', dpi=200, id=0):
        """Render image with plot"""
        if not self.prepared: 
            raise Exception("Failed to save plot: it isn't prepared yet")
        filename = f'MandSet_{id}_[{self.xmin};{self.xmax}]x[{self.ymin};{self.ymax}]_{self.width}x{self.height}_{self.max_iter}i.png'
        plt.savefig(f'{destination}/{filename}', dpi=dpi, bbox_inches='tight');
        
    def show_plot(self):
        """Generate UI window with plot"""
        if not self.prepared: 
            raise Exception("Failed to save plot: it isn't prepared yet")
        plt.show()
        
    def clean_up(self):
        plt.close()
    