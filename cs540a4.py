
from collections import deque

def lru_page_faults(reference_string, frame_number):
    #set keeps track of pages currently in memory
    page_set = set()
    # deque represents page frames
    page_frames = deque()
    # counter tracks page faults
    faults = 0
    
    print("For LRU Algorithm:")
    
    for i, page in enumerate(reference_string):
        if page not in page_set:
            faults += 1
            # if the number of frames is equal to the frame limit
            if len(page_frames) == frame_number:
                # remove the least recently used page from the frames and set
                least_recently_used_page = page_frames.pop()
                page_set.remove(least_recently_used_page)
            # add the current page to the front of the frames and set
            page_frames.appendleft(page)
            page_set.add(page)
            print(f"• Step {i + 1}: Page fault ({page}) - Page Table: {page_set}, Frames: {list(page_frames)}, Faults: {faults}")
        else:
            # if the page is already in memory, remove it from its current position
            # and add it to the front of the frames to indicate it was recently used
            page_frames.remove(page)
            page_frames.appendleft(page)
    print(f"• Total Page Faults: {faults}")

def fifo_page_faults(reference_string, frame_number):
    # set keeps track of pages currently in memory
    page_set = set()
    # deque represents page frames
    page_frames = deque()
    # counter to track page faults
    faults = 0
    print("For FIFO Algorithm:")
    for i, page in enumerate(reference_string):
        if page not in page_set:
            faults += 1
            # if the number of frames is equal to the frame limit
            if len(page_frames) == frame_number:
                # remove oldest page from the frames and set
                oldest_page = page_frames.pop()
                page_set.remove(oldest_page)
            # add the current page to the front of the frames and set
            page_frames.appendleft(page)
            page_set.add(page)
            print(f"• Step {i + 1}: Page fault ({page}) - Page Table: {page_set}, Frames: {list(page_frames)}, Faults: {faults}")
    print(f"• Total Page Faults: {faults}")

def optimal_page_faults(reference_string, frame_number):
    # set keeps track of pages currently in memory
    page_set = set()
    # deque represents page frames
    page_frames = deque()
    # counter tracks page faults
    faults = 0
    print("For Optimal Algorithm:")
    for i, page in enumerate(reference_string):
        if page not in page_set:
            faults += 1
            # if the number of frames is equal to the frame limit
            if len(page_frames) == frame_number:
                # find the page that will not be used furthest in the future
                future_indices = {p: len(reference_string) for p in page_frames}
                for j in range(i + 1, len(reference_string)):
                    if reference_string[j] in future_indices:
                        future_indices[reference_string[j]] = j
                evict_page = max(future_indices, key=future_indices.get)
                page_frames.remove(evict_page)
                page_set.remove(evict_page)
            # Add the current page to the frames and set
            page_frames.append(page)
            page_set.add(page)
            print(f"• Step {i + 1}: Page fault ({page}) - Page Table: {page_set}, Frames: {list(page_frames)}, Faults: {faults}")
    print(f"• Total Page Faults: {faults}")

reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_number = 4

# run algorithms
lru_page_faults(reference_string, frame_number)
fifo_page_faults(reference_string, frame_number)
optimal_page_faults(reference_string, frame_number)