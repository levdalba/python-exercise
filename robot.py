# around1 - apple

# while True:
#     if object_here():
#         take()
#     elif not front_is_clear():
#         turn_left()
#     elif front_is_clear():
#         move()
#     if at_goal():
#         break

# around2

# put()
# while True:
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         turn_left()
#     if right_is_clear():
#         turn_left()
#         turn_left()
#         turn_left()
#     if object_here():
#         break

# around3

# put()
# while True:
#     if wall_in_front():
#         turn_left()
#     if front_is_clear():
#         move()
#     if right_is_clear():
#         turn_left()
#         turn_left()
#         turn_left()
#     if not right_is_clear() and wall_in_front():
#         turn_left()
#     if object_here():
#         break

# around4

# put()
# while True:
#     while wall_in_front():
#         turn_left()
#     if front_is_clear():
#         move()
#     if right_is_clear():
#         turn_left()
#         turn_left()
#         turn_left()
#     if not right_is_clear() and wall_in_front():
#         turn_left()
#     if object_here():
#         break

# center 1

# put()
# def turn_around():
#     turn_left()
#     turn_left()
# while True:
#     if object_here():
#         move()
#         move()
#         if wall_in_front():
#             turn_around(); move();move();take();turn_around();move();put();break
#         if object_here():
#             take()
#             turn_around()
#             move()
#             move()
#             take()
#             turn_around()
#             move()
#             put()
#             break

#         else: continue

#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         put() and turn_around()
#     if object_here():
#         take(); turn_around(); move(); put()

# center2
# def turn_around():
#     turn_left()
#     turn_left()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def horizontal():
#     while True:
#         if object_here():
#             move()
#             move()
#             if wall_in_front():
#                 turn_around()
#                 move()
#                 move()
#                 take()
#                 turn_around()
#                 move()
#                 put()
#                 break

#             if object_here():
#                 take()
#                 turn_around()
#                 move()
#                 move()
#                 take()
#                 turn_around()
#                 move()
#                 put()
#                 break

#             else: continue

#         if front_is_clear():
#             move()
#         elif wall_in_front():
#             put() and turn_around()
#         if object_here():
#             take(); turn_around(); move(); put()
# put()
# turn_left()
# if wall_in_front():
#     turn_right()
#     horizontal()

# elif front_is_clear():
#     turn_right()
#     while True:
#         if object_here():
#             move()
#             move()
#             if wall_in_front():
#                 turn_around(); move();move();take();turn_around();move();put();break
#             if object_here():
#                 take()
#                 turn_around()
#                 move()
#                 move()
#                 take()
#                 turn_around()
#                 move()
#                 put()
#                 turn_left()
#                 horizontal()
#                 break


#             else: continue

#         if front_is_clear():
#             move()
#         elif wall_in_front():
#             put() and turn_around()
#         if object_here():
#             take(); turn_around(); move(); put()

# Harveest1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def right():
#     move()
#     turn_right()
#     move()
#     turn_right()
# def left():
#     move()
#     turn_left()
#     move()
#     turn_left()
# def taking():
#     for i in range(6):
#         move()
#         take()
# def firstmove():
#     move()
#     move()
#     turn_left()
#     move()
# firstmove()
# taking()
# right()
# taking()
# left()
# taking()
# right()
# taking()
# left()
# taking()
# right()
# taking()

# harvest2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def right():
#     move()
#     turn_right()
#     move()
#     turn_right()
# def left():
#     move()
#     turn_left()
#     move()
#     turn_left()
# def taking():
#     for i in range(6):
#         move()
#         for j in range(3):
#             if object_here():
#                 take()
#             else: continue

# def firstmove():
#     move()
#     move()
#     turn_left()
#     move()
# firstmove()
# taking()
# right()
# taking()
# left()
# taking()
# right()
# taking()
# left()
# taking()
# right()
# taking()

# harvest 3

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def right():
#     move()
#     turn_right()
#     move()
#     turn_right()
# def left():
#     move()
#     turn_left()
#     move()
#     turn_left()
# def taking():
#     for i in range(6):
#         move()
#         for j in range(3):
#             if object_here():
#                 take()
#             else: continue
#         put()
# def firstmove():
#     move()
#     move()
#     turn_left()
#     move()
# firstmove()
# taking()
# right()
# taking()
# left()
# taking()
# right()
# taking()
# left()
# taking()
# right()
# taking()

# hurdle1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def func():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for i in range(6):
#     func()

# hurdle2

# def funcfunc():
#     func()
#     if at_goal():
#         done()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def func():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for i in range(6):
#     funcfunc()

# hurdle3

# def func():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# for i in range(10):
#     if at_goal():
#         break
#     else:
#         if front_is_clear():
#             move()
#         while wall_in_front():
#             func()

# hurdle 4

# def func():
#     turn_left()
#     move()
#     turn_right()
#     while wall_in_front():
#         turn_left()
#         move()
#         turn_right()
#     move()
#     turn_right()
#     move()
#     while front_is_clear():
#         move()
#     turn_left()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# for i in range(10):
#     if at_goal():
#         break
#     else:
#         if front_is_clear():
#             move()
#         while wall_in_front():
#             func()

# maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while front_is_clear():
#     move()
#     turn_left()


# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     elif wall_in_front() and right_is_clear():
#         turn_right()
#         move()
#     else:
#         turn_left()

# newspaper 0
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# take()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# put()
# turn_left()
# turn_left()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# done()

# newspaper1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# take()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# put("star")
# for i in range(3):
#     if object_here("token"):
#         take("token")
#     else:
#         continue
# turn_left()
# turn_left()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# turn_right()
# move()
# move()
# turn_left()
# move()
# done()

# rain 0

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around():
#     turn_left()
#     turn_left()
# move()
# move()
# move()
# move()
# move()
# move()
# build_wall()
# turn_around()
# move()
# move()
# move()
# move()
# move()
# done

# rain 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around():
#     turn_left()
#     turn_left()
# def build_move():
#     if wall_in_front():
#         turn_left()
#     elif wall_on_right():
#         move()
#     elif at_goal():
#         done()
#     else:
#         turn_right()
#         build_wall()
# think(0)
# move()
# turn_right()
# move()
# repeat 60:
#     build_move()

# rain2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around():
#     turn_left()
#     turn_left()
# def build_move():
#     if wall_in_front():
#         turn_left()
#     elif wall_on_right():
#         move()
#     elif at_goal():
#         done()
#     elif not wall_on_right():
#         move()
#         turn_right()
#         if not front_is_clear():
#             turn_right()
#             move()
#             turn_left()
#             build_wall()
#         else:
#             turn_right()
#             move()
#             turn_left()
#             move()
# think(0)
# move()
# move()
# move()
# turn_right()
# move()
# repeat 60:
#     build_move()

# storm 1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around():
#     turn_left()
#     turn_left()

# for i in range(5):
#     move()
#     for j in range(3):
#         if object_here():
#             take()
#         else: continue
# turn_around()
# for i in range(5):
#     move()
# turn_right()
# for i in range(8):
#     if carries_object():
#         toss()
#     else:
#         done()

# storm 2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around():
#     turn_left()
#     turn_left()
# def moving():
#     for i in range(5):
#         move()
#         for i in range(3):
#             if object_here():
#                 take()
#             else:
#                 continue
# moving()
# turn_left()
# moving()
# turn_left()
# moving()
# turn_left()
# move()
# turn_left()
# for i in range(3):
#             if object_here():
#                 take()
#             else:
#                 continue
# moving()
# turn_right()
# move()
# turn_right()
# for i in range(3):
#             if object_here():
#                 take()
#             else:
#                 continue
# moving()
# turn_left()
# move()
# for i in range(3):
#             if object_here():
#                 take()
#             else:
#                 continue
# turn_left()
# moving()
# turn_right()
# move()
# turn_right()
# for i in range(4):
#         move()
#         for i in range(3):
#             if object_here():
#                 take()
#             else:
#                 continue
# for i in range(15):
#         if carries_object():
#             toss()
#         else:
#             turn_left()
#             move()
#             turn_right()
#             move()
#             done()
