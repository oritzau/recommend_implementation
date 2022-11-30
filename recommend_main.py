#This implementation is a bit finicky, so I recommend (haha) not implementing the "done" utility as it was a headache and required
#some fairly stupid try except use.

#Instead, use a while loop and cover the conditions of a user entering a name not in the list and you should be set

user_not_done = True
    user_not_in_list = True
    while user_not_done:
        recommended_list = []
        while user_not_in_list:
            print(names)
            suggestions_for = input('Enter Name: ')
            if suggestions_for in names or suggestions_for.lower() == 'done':
                user_not_in_list = False
            if suggestions_for.lower() == 'done':
                user_not_done = False
            elif suggestions_for not in names:
                print('Sorry, that name is not in our library')
        try:
            suggestion_for_index = names.index(suggestions_for)
            suggestion_to_index = recommend(suggestion_for_index)
            for a, b in enumerate(user_ratings[suggestion_to_index]):
                if user_ratings[suggestion_for_index][a] == 0 and (len(recommended_list) < 6):
                    if user_ratings[suggestion_to_index][a] == 5:
                        recommended_list.append(a)
            print()
            print(f'For {suggestions_for} we recommend:')
            if len(recommended_list) != 0:
                for book_index in recommended_list:
                    print(book_list[book_index].title)
            else:
                print('No books found')
            print()
            user_not_in_list = True
            if suggestions_for.lower() == 'done':
                user_not_done = False
        except ValueError:
            if suggestions_for.lower() == 'done':
                print('Thank you for using Recommend.', end = '\n' * 2)
                user_not_done = False