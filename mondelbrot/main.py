
from core import Core

def main():
    LOW_DPI = 200
    HIGH_DPI = 3000
    LOW_HW = 600
    HIGH_HW = 3000
    MAX_ITER = 2000
    HW = HIGH_HW
    models = [
        # Core(-2, 0.5, HW, -1.25, 1.25, HW),
        # Core(-1.8, -1.74, HW, -0.03, 0.03, HW), # хвостик
        # Core(-1.78, -1.76, HW, -0.01, 0.01, HW), # приближение хвостика
        # Core(-1.77, -1.7675, HW, 0.0010, 0.0035, HW), # щель в хвостике
        # Core(-1.7775, -1.7745, HW, 0.0038, 0.0068, HW), # красиво на краю хвостика
        Core(-0.12, 0.18, HW, 0.62, 0.92, HW)
    ]
    render_pics(models, HIGH_DPI, MAX_ITER)

def render_pics(models : list, dpi, max_iter):
    for idx, model in enumerate(models):
        print(f"Model {idx}: Rendering...")
        model.set_max_iter(max_iter)
        model.run()
        model.save_plot(id=idx+1, dpi=dpi)
        print(f"Model {idx}: Rendering completed")
        # model.show_plot()
        model.clean_up()

if __name__ == '__main__':
    main()