#Python Sets
colors = {'red', 'green'}
colors.add('blue')
colors.update(['yellow', 'purple', 'orange'])
colors.remove('green')
colors.discard('pink')
popped = colors.pop()
print(f"popped element: {popped}")
print(f"after removals: {colors}")
