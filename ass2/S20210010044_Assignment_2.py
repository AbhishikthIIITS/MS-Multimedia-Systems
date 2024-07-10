import pyglet
from PIL import Image, ImageDraw

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Ball properties
BALL_RADIUS = 50
BALL_COLOR = (20, 59, 200)

# Initial ball position and velocity
ball_x, ball_y = WIDTH // 2, BALL_RADIUS
ball_vy = -200  # Vertical velocity only

# Create a window
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

# Initialize variables for capturing frames
frames = []

def update(dt):
    global ball_y, ball_vy
    ball_y += ball_vy * dt
    if ball_y + BALL_RADIUS >= HEIGHT:
        ball_y = 2 * (HEIGHT - BALL_RADIUS) - ball_y
        ball_vy = -ball_vy
    elif ball_y - BALL_RADIUS <= 0:
        ball_y = 2 * BALL_RADIUS - ball_y
        ball_vy = -ball_vy

    # Create a blank image
    frame = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(frame)

    # Draw the ball on the image
    draw.ellipse((ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), fill=BALL_COLOR)

    frames.insert(0, frame)  # Insert the new frame at the beginning of the list


# Draw function
@window.event
def on_draw():
    window.clear()
    ball = pyglet.shapes.Circle(ball_x, ball_y, BALL_RADIUS, color=BALL_COLOR)
    ball.draw()

# Schedule the update function
pyglet.clock.schedule_interval(update, 1/60)

# Run the application
pyglet.app.run()

# Save the captured frames as an animated GIF
frames[0].save('bounceBall123.gif', save_all=True, append_images=frames[1:], duration=3000/60, loop=0)