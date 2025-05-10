# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

# Reset
reset = "\033[0m"

# Regular Colors
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
gray = "\033[0;90m"

# Bold
black_bold = "\033[1;30m"
red_bold = "\033[1;31m"
green_bold = "\033[1;32m"
yellow_bold = "\033[1;33m"
blue_bold = "\033[1;34m"
purple_bold = "\033[1;35m"
cyan_bold = "\033[1;36m"
white_bold = "\033[1;37m"
gray_bold = "\033[1;90m"

# Underline
black_underline = "\033[4;30m"
red_underline = "\033[4;31m"
green_underline = "\033[4;32m"
yellow_underline = "\033[4;33m"
blue_underline = "\033[4;34m"
purple_underline = "\033[4;35m"
cyan_underline = "\033[4;36m"
white_underline = "\033[4;37m"
gray_underline = "\033[4;90m"

# Background
black_background = "\033[40m"
red_background = "\033[41m"
green_background = "\033[42m"
yellow_background = "\033[43m"
blue_background = "\033[44m"
purple_background = "\033[45m"
cyan_background = "\033[46m"
white_background = "\033[47m"
gray_background = "\033[100m"

# High Intensity
black_high = "\033[0;90m"
red_high = "\033[0;91m"
green_high = "\033[0;92m"
yellow_high = "\033[0;93m"
blue_high = "\033[0;94m"
purple_high = "\033[0;95m"
cyan_high = "\033[0;96m"
white_high = "\033[0;97m"

# Bold High Intensity
black_bold_high = "\033[1;90m"
red_bold_high = "\033[1;91m"
green_bold_high = "\033[1;92m"
yellow_bold_high = "\033[1;93m"
blue_bold_high = "\033[1;94m"
purple_bold_high = "\033[1;95m"
cyan_bold_high = "\033[1;96m"
white_bold_high = "\033[1;97m"

# High Intensity backgrounds
black_background_high = "\033[0;100m"
red_background_high = "\033[0;101m"
green_background_high = "\033[0;102m"
yellow_background_high = "\033[0;103m"
blue_background_high = "\033[0;104m"
purple_background_high = "\033[0;105m"
cyan_background_high = "\033[0;106m"
white_background_high = "\033[0;107m"


def colorize(text: str, color: str) -> str:
  """
  Colorize text with the given color

  Args:
      text: Text to colorize
      color: Color code to apply

  Returns:
      Colored text string
  """
  return f"{color}{text}{reset}"


def print_color(text: str, color: str, end: str = '\n') -> None:
  """
  Print colored text

  Args:
      text: Text to print
      color: Color code to use
      end: Ending character (default: newline)
  """
  print(colorize(text, color), end=end)