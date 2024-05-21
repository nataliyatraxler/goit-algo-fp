import matplotlib.pyplot as plt
import math

def draw_tree(ax, x, y, branch_length, angle, level):
    if level == 0:
        return
    
    x2 = x + branch_length * math.cos(math.radians(angle))
    y2 = y + branch_length * math.sin(math.radians(angle))
    
    ax.plot([x, x2], [y, y2], color='brown', lw=level)

    new_length = branch_length * math.sqrt(2) / 2

    draw_tree(ax, x2, y2, new_length, angle - 45, level - 1)
    draw_tree(ax, x2, y2, new_length, angle + 45, level - 1)

def main():
    recursion_level = int(input("Enter the recursion level: "))
    branch_length = 100

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    draw_tree(ax, 0, 0, branch_length, 90, recursion_level)

    plt.show()

if __name__ == "__main__":
    main()
