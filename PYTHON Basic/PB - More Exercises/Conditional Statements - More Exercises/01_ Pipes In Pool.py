volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

litеrs_pipe_1 = pipe_1 * hours
litеrs_pipe_2 = pipe_2 * hours
total_liters = litеrs_pipe_1 + litеrs_pipe_2

percent_liters = (total_liters / volume) * 100
percent_liters_pipe_1 = (litеrs_pipe_1 / total_liters) * 100
percent_liters_pipe_2 = (litеrs_pipe_2 / total_liters) * 100

if volume >= total_liters:
    print(f"The pool is {percent_liters:.2f}% full. Pipe 1: {percent_liters_pipe_1:.2f}%. Pipe 2: {percent_liters_pipe_2:.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {total_liters - volume:.2f} liters.")