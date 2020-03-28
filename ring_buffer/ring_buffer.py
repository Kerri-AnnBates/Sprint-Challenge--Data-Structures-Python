from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		#  When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.
		# [ 'oldest', ... , 'recent' ]
		# [ head, ... , tail ]
		# [ 'a', 'b', 'c' ]

		if len(self.storage) is not self.capacity:
			self.storage.add_to_tail(item)

			# set current to the oldest item
			self.current = self.storage.head

		else:
			if self.current.next:  # If not the tail
				next_node = self.current.next
			else: 
				# if tail make the next node the head
				next_node = self.storage.head
			
			# overwrite the oldest item which is initially the head (current)
			self.current.value = item
			self.current = next_node

	def get(self):
		# Note:  This is the only [] allowed
		list_buffer_contents = []

		# TODO: Your code here
		if len(self.storage):

			curr = self.storage.head

			while curr:
				list_buffer_contents.append(curr.value)
				curr = curr.next

		return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
	def __init__(self, capacity):
		pass

	def append(self, item):
		pass

	def get(self):
		pass


# Set current to the oldest item
# if current is not the tail
# set the next storage item to current
#  set the prev to the new item
#  set storage.next to storage.next.next
