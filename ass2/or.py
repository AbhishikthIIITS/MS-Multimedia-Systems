import pyglet

window = pyglet.window.Window(width=800, height=600)

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

pyglet.clock.schedule_interval(update, 1/120.0)  # Update at 120 Hz

pyglet.app.run()

