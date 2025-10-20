from core import Core

def main():
    MAX_ITER = 1000
    SIZE = 1000
    DPI = 1000
    models = [
        Core(-1.5, 1.5, SIZE, -1.5, 1.5, SIZE, complex(-0.701977777790331213, 0.3143338473)),
        Core(-1.5, 1.5, SIZE, -1.5, 1.5, SIZE, complex(-0.1997777790331213, 0.8143338473)),
        Core(-1.5, 1.5, SIZE, -1.5, 1.5, SIZE, complex(-0.457659990235729384, 0.5926258658473)),
        Core(0.05, 0.15, SIZE, -0.82, -0.72, SIZE, complex(-0.457659990235729384, 0.5926258658473))
    ]
    
    run_models(models, MAX_ITER, DPI)
    
def run_models(models, max_iter, dpi):
    for (idx, model) in enumerate(models):
        print(f'Model {idx} rendering...')
        model.set_max_iter(max_iter)
        model.run()
        model.save_plot(id=idx, dpi=dpi)
        print(f'Model {idx} successfully rendered!')
        
if __name__ == '__main__':
    main()