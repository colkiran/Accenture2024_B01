
glbX = 100

def fun(x):
    global glbX
    print(f"x :{x}")
    print(f"Inside :{glbX}")
    glbX += 400

print(f"Before the function call :{glbX}")

fun(10)

print(f"After the function call :{glbX}")
