import pyglet
from PIL import Image, ImageSequence

window = pyglet.window.Window(width=800, height=600)
frames = []

ball_image = pyglet.resource.image('ball.jpeg')
ball_sprite = pyglet.sprite.Sprite(ball_image, x=400, y=300)

ball_speed = 300  # pixels per second
ball_direction = 1  # 1 for up, -1 for down

def update(dt):
    global ball_direction
    ball_sprite.y += ball_speed * ball_direction * dt

    if ball_sprite.y >= window.height - ball_sprite.height or ball_sprite.y <= 0:
        ball_direction *= -1

@window.event
def on_draw():
    window.clear()
    ball_sprite.draw()
    buffer = pyglet.image.get_buffer_manager().get_color_buffer()
    image_data = buffer.get_image_data()
    image = Image.frombytes('RGBA', (window.width, window.height), image_data.get_data('RGBA', image_data.width * 4))
    frames.append(image)

pyglet.clock.schedule_interval(update, 1/120.0)  # Update at 120 Hz

pyglet.app.run()

# Save the frames as an animated GIF
frames[0].save('animation.gif', save_all=True, append_images=frames[1:], loop=0, duration=int(1/120.0 * 1000))
