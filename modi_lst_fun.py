def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\n")
    for completed_model in reversed(completed_models):

        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)