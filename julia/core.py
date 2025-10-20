import numpy as np
import matplotlib.pyplot as plt

class Core:
    """Main class represents evaluating model"""
    def __init__(self, xmin, xmax, width, ymin, ymax, height, complex_const):
        self.xmin = xmin
        self.xmax = xmax
        self.width = width
        self.ymax = ymax
        self.ymin = ymin
        self.height = height
        self.max_iter = 500 # defalut value
        self.complex_const = complex_const
        self.prepared = False   

    def set_max_iter(self, value):
        self.max_iter = value
        
    def run(self):
        """Prepare&process data for rendering"""
        y, x = np.ogrid[self.ymax:self.ymin:self.height*1j, self.xmin:self.xmax:self.width*1j]
        Z = x + y * 1j # complex plate
        N = np.full((self.height, self.width), self.max_iter, dtype=int) # escaping iteration
        M = np.full((self.height, self.width), True, dtype=bool) # mask (not esacped yet) 
        C = np.full((self.height, self.width), self.complex_const, dtype=complex) # c const

        for i in range(self.max_iter):
            Z[M] = Z[M]**2 + C[M] # update if hasn't escaped 
            escaped = np.abs(Z) > 2.0
            escaped_now = escaped & M
            N[escaped_now] = i + 1
            M[escaped] = False
            if not np.any(M): # if there is no points to track
                break

        self.__prepare_plot(Core.__colorize(N, Z, self.max_iter))
    
    def __prepare_plot(self, nu):
        plt.imshow(nu, extent=[self.xmin, self.xmax, self.ymin, self.ymax], cmap='viridis')
        plt.title(f'Julia set for c = {self.complex_const.real:.4f} + {self.complex_const.imag:.4f}i')
        plt.xlabel("Re(c)")
        plt.ylabel("Im(c)")
        plt.colorbar(label='Iterations to Escape(normalized)')
        self.prepared = True
        
    def __colorize(N, Z, max_iter):
        """Used to make color smoothing"""
        nu2d = np.zeros(N.shape, dtype=float) # future nu in 2D
        mask_escaped = N < max_iter
        N_escaped = N[mask_escaped]
        Z_escaped = Z[mask_escaped]
        
        log_Z_escaped = np.log(np.log(np.abs(Z_escaped))) / np.log(2)
        nu = N_escaped + 1 - log_Z_escaped
        nu_normalized = np.log(nu) / np.log(max_iter);
        nu2d[mask_escaped] = nu_normalized
        return nu2d
    
    def save_plot(self, destination='./julia/render', dpi=200, id=0):
        """Render image with plot"""
        if not self.prepared: 
            raise Exception("Failed to save plot: it isn't prepared yet")
        filename = f'JuliaSet_{id}_[{self.xmin};{self.xmax}]x[{self.ymin};{self.ymax}]_{self.width}x{self.height}_{self.max_iter}i.png'
        plt.savefig(f'{destination}/{filename}', dpi=dpi, bbox_inches='tight');
        plt.close()
    
    def show(self):
        if not self.prepared: 
            raise Exception("Failed to save plot: it isn't prepared yet")
        plt.show()
