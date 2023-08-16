from main import *


def update(frame):
    s_hat_slice = s_hat[::-1][:frame + 1]

    s_hat_temp = np.zeros_like(s_hat)
    s_hat_temp[:frame + 1] = s_hat_slice[::-1]

    s2 = np.fft.ifft(s_hat_temp)

    ax.clear()
    ax.plot(np.abs(s2))

    ax.set_ylim([0, np.max(np.abs(s2))])


x = np.array([x for x in range(64)])
s = np.array(x*np.sin(0.39*x)**2)
s[16:40] = 0
s_hat_abs = np.abs(fft.fft(s))
s_hat = fft.fft(s)

fig, ax = plt.subplots()

anim = FuncAnimation(fig, update, frames=64, interval=1000)
anim.save('reversed_slices_animation.gif', writer='imagemagick')