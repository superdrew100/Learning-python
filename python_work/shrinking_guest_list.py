#made a guest list and did a bunch of changes to it using insert() and append() and then printed a new set of invatations
guest_list=["jhon", "james bond", "abraham lincon"]
guest_list_middle=round(len(guest_list)/2)
removed_guests=[]

print(f'Dear, {guest_list[0].title()}, I would like to invite you to a dinner party.')
print(f'Dear, {guest_list[1].title()}, I would like to invite you to a dinner party.')
print(f'Dear, {guest_list[2].title()}, I would like to invite you to a dinner party.')
couldt_arrive= guest_list.pop(1)
print(f"I'm sorry to have to mention but {couldt_arrive} was unable to ariive at the dinner party.")
print(f'Dear, {guest_list[0].title()}, I would like to invite you to a dinner party.')
print(f'Dear, {guest_list[1].title()}, I would like to invite you to a dinner party.')
print('Informing everyone that I have found a larger table so I can fist more guests')
guest_list.insert(0, 'jhon wilks booth')
guest_list.insert(guest_list_middle, "Cast from Jersy shores")
guest_list.append("Luke skywalker")
print(guest_list)
print(len(guest_list))
print(f'Dear {guest_list[0]}, I have have found a bigger table so now ic an invite you!')
print(f'Dear {guest_list[1]}, I have have found a bigger table so now ic an invite you!')
print(f'Dear {guest_list[2]}, I have have found a bigger table so now ic an invite you!')
print(f'Dear {guest_list[3]}, I have have found a bigger table so now ic an invite you!')
print(f'Dear {guest_list[4]}, I have have found a bigger table so now ic an invite you!')
# you can now only invite two guests
print('Sorry to inform you, But I can only invite 2 peopl over for dinner now.')
removed_guests.append(guest_list.pop(0))
removed_guests.append(guest_list.pop(1))
removed_guests.append(guest_list.pop(2))
print(f'You have removed {removed_guests} from the invite list.')
print(f'Dear {guest_list[0]} Just letting you know that your still invited.')
print(f'Dear {guest_list[1]} Just letting you know that your still invited.')
del(guest_list[0])
del(guest_list[0])
print(guest_list)



