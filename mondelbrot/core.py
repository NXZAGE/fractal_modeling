import numpy as np
import matplotlib.pyplot as plt

class Core():
    def __init__(self, xmin, xmax, width, ymin, ymax, height):
        self.xmin = xmin
        self.xmax = xmax
        self.width = width
        self.ymax = ymax
        self.ymin = ymin
        self.height = height
        self.max_iter = 1000
        pass
    
    def run(self):
        x = np.linspace(self.xmin, self.xmax, self.width)
        # y = np.linspace(self.ymin, self.ymax, self.height) # Ошибка
        y = np.linspace(self.ymax, self.ymin, self.height) # ymax сверху, ymin снизу

        # 2. Создание двумерной сетки (координат)
        # 'ij' обеспечивает, что первая ось (i) соответствует y (строкам), а вторая (j) - x (столбцам)
        X, Y = np.meshgrid(x, y)

        # 3. Комплексная плоскость C
        C = X + 1j * Y  # '1j' - мнимая единица в NumPy
        
        Z = np.zeros(C.shape, dtype=np.complex128)
        N = np.zeros(C.shape, dtype=np.int32)
        
        for i in range(self.max_iter):
            # 1. Находим точки, которые еще не убежали (|Z| <= 2)
            # np.abs(Z) > 2.0  -> Булев массив (True для убежавших)
            # ~ (тильда) -> Инвертирует булев массив (True для НЕ убежавших)
            mask_not_escaped = np.abs(Z) <= 2.0

            # Если ни одна точка не осталась, выходим
            if not np.any(mask_not_escaped):
                break

            # 2. Обновляем Z только для НЕ убежавших точек
            Z[mask_not_escaped] = Z[mask_not_escaped]**2 + C[mask_not_escaped]

            # 3. Фиксируем счетчик итераций (i+1) для тех, кто убежал НА ЭТОЙ итерации
            # (mask == False) AND (предыдущее N == 0)
            # Более простой способ:
            # Увеличиваем N для всех точек, которые все еще внутри (mask == True)
            mask_escaped_now = (mask_not_escaped) & (np.abs(Z) > 2.0)
            N[mask_escaped_now] = i + 1
            
        mask_escaped = N > 0 
        N_escaped = N[mask_escaped]
        Z_escaped = Z[mask_escaped]
        
        log_Z_escaped = np.log(np.log(np.abs(Z_escaped))) / np.log(2)
        nu = N_escaped + 1 - log_Z_escaped
        nu_normalized = np.log(nu) / np.log(self.max_iter);
        # nu_normalized = nu
        self.show_plot(N, nu_normalized)
        
    def show_plot(self, N, nu):
        final_image_data = np.zeros(N.shape, dtype=float)

        # Заполняем только убежавшие точки масштабированными значениями
        final_image_data[N > 0] = nu

        # Возвращаем/отображаем final_image_data
        plt.imshow(final_image_data, cmap='hot', extent=[self.xmin, self.xmax, self.ymin, self.ymax])

        # cmap - цветовая карта. 'twilight_shifted' - популярна для Мандельброта.

        # extent - устанавливает оси, чтобы отображать реальные координаты (Re и Im)

        plt.xlabel("Re(c)")

        plt.ylabel("Im(c)")

        plt.title(f"Mandelbrot Set ({self.width}x{self.height}, {self.max_iter} iter)")

        plt.colorbar(label="Iterations to Escape")

        plt.show()
        
        