
from core import Core

def main():
    print('hello world')
    core = Core(-2, 1, 600, -1.5, 1.5, 600)
    core = Core(-1.8, -1.7, 600, -0.05, 0.05, 600)
    core = Core(-1.8, -1.76, 600, -0.02, 0.02, 600)
    core = Core(-1.78, -1.76, 600, -0.01, 0.01, 600)
    # core = Core(-2, -1.5, 600, -1.5, -1, 600)
    # core = Core(-0.5, 0.5, 600, -1.2, -0.2, 600)
    # core = Core(-0.2, 0.2, 600, -0.8, -0.4, 600)
    # core = Core(-0.2, -0.00, 600, -0.25, -0.05, 600)
    core.run()
    pass

if __name__ == '__main__':
    main()