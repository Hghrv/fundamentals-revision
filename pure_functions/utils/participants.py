def participants(goats):
    #copy the argument to ensure purity
    goats_copy = [goat for goat in goats]
    #initialising the output
    output =[]
    #append name dictionary to output and return output
    for goat in goats_copy:
        output.append({key: goat[key] for key in goat if key == 'name'})
    return output