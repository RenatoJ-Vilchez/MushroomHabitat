gill_size = input(
  "Input gill size n for narrow, b for broad or enter to skip: ")
stalk_shape = input(
  "Input stalk shape e for enlarged, t for tapered or enter to skip: ")
classofmush = input(
  "Input class p for poisonous e for edible or enter to skip: ")
cap_shape = input(
  "Input cap shape c for convex, b for bell, s for sunken, f for flat or enter to skip: "
)
gill_color = input(
  "Input gill color bl for black, br for brown, g for gray, p for pink, w for white, c for chocolate or enter to skip: "
)
cap_color = input(
  "Input cap color br for brown, y for yellow, w for white, g for gray or enter to skip: "
)
population = input(
  "Input population sc for scattered, n for numerous, a for abundant, se for several, and so for solitary or enter to skip:"
)
odor = input(
  "Input odor p for pungent, al for almond, an for anise, n for none or enter to skip: "
)
cap_surface = input(
  "Input cap surface sm for smooth, sc for scaley, f for fiberous or enter to skip: "
)

if gill_size.lower() == "n" and stalk_shape.lower() == "t":
  print("This mushroom's habitat could be woods")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush == "e":
  print("This mushroom's habitat could be urban")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush == "p" and cap_shape == "f":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush == "p" and cap_shape == "s" or "b":
  print("This mushroom's habitat could be urban")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush.lower() == "p" and cap_shape.lower(
) == "c" and gill_color.lower() == "c" or "w" or "g" or "bl":
  print("This mushroom's habitat could be urban")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush.lower() == "p" and cap_shape.lower(
) == "c" and gill_color.lower() == "p":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush.lower() == "p" and cap_shape.lower(
) == "c" and gill_color.lower() == "br" and cap_color.lower() == "br":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "n" and stalk_shape.lower(
) == "e" and classofmush.lower() == "p" and cap_shape.lower(
) == "c" and gill_color.lower() == "br" and cap_color.lower(
) == "y" or "w" or "g":
  print("This mushroom's habitat could be urban")

elif gill_size.lower() == "b" and population.lower(
) == "sc" and cap - shape.lower() == "c" or "s" or "f":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "b" and population.lower(
) == "sc" and cap - shape.lower() == "b" and odor.lower(
) == "p" or "an" or "n":
  print("This mushroom's habitat could be meadows")
elif gill_size.lower() == "b" and population.lower(
) == "sc" and cap - shape.lower() == "b" and odor.lower(
) == "al" and cap_surface.lower() == "sm" or "f":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "b" and population.lower(
) == "sc" and cap - shape.lower() == "b" and odor.lower(
) == "al" and cap_surface.lower() == "sc" and cap_color.lower() == "y":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "b" and population.lower(
) == "sc" and cap - shape.lower() == "b" and odor.lower(
) == "al" and cap_surface.lower() == "sc" and cap_color.lower(
) == "br" or "w" or "g":
  print("This mushroom's habitat could be meadows")

elif gill_size.lower() == "b" and population.lower() == "a" or "se":
  print("This mushroom's habitat could be grassy")

elif gill_size.lower() == "b" and population.lower(
) == "n" and cap_color == "br" or "w" or "g":
  print("This mushroom's habitat could be meadows")
elif gill_size.lower() == "b" and population.lower(
) == "n" and cap_color == "y" and cap_shape == "c":
  print("This mushroom's habitat could be meadows")
elif gill_size.lower() == "b" and population.lower(
) == "n" and cap_color == "y" and cap_shape == "b" or "s" or "f":
  print("This mushroom's habitat could be grassy")

elif gill_size.lower() == "b" and population.lower(
) == "so" and gill_color == "bl" or "g" or "p" or "c":
  print("This mushroom's habitat could be paths")
elif gill_size.lower() == "b" and population.lower(
) == "so" and gill_color == "br" and cap_shape == "c":
  print("This mushroom's habitat could be paths")
elif gill_size.lower() == "b" and population.lower(
) == "so" and gill_color == "br" and cap_shape == "b" or "s" or "f":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "b" and population.lower(
) == "so" and gill_color == "w" and odor == "p" or "an" or "n":
  print("This mushroom's habitat could be grassy")
elif gill_size.lower() == "b" and population.lower(
) == "so" and gill_color == "w" and odor == "al":
  print("This mushroom's habitat could be paths")
