import cx_Freeze

executables = [cx_Freeze.Executable("game-tutorial.py")]

cx_Freeze.setup(
    name="Space Invaders",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["alien.png", "background.wav", "bullet.png", "explosion.wav", "laser.wav", "space-invader.png", "space-invaders.png"]}},
    executables = executables

    )