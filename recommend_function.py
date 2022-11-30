#This is how I defined the recommend function, user_ratings is defined within the main function, hence the underlines

def recommend(reader): #takes reader as argument (numerical index of reader in list of names)
    similarity_list = [] #initializes empty list of similar readers
    for row in user_ratings: #iterates through list of user ratings
        similarity = np.dot(user_ratings[reader], row) #np.dot(x, y) computes the dot product of x and y. 
        similarity_list.append(similarity) #appends the dot product to similarity list
    similarity_second_max = sorted(similarity_list)[-2] #sorts the similarity list and accesses the second to last index
    #the last index will always the index of the reader, as they are most similar to themselves
    similarity_max_index = similarity_list.index(similarity_second_max) #saves the index of most similar reader as a value
    return similarity_max_index #returns said value