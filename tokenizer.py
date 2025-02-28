from typing import Dict, List, Optional, Pattern, Set, Tuple, Union



def get_stats(ids: List[int], counts: Optional[Dict[int, int]]=None) -> Dict[int, int]:
    """
    Iterates over the list of ids and counts the occurrences of each pair of ids.
    If counts is provided, it will be updated with the counts of the ids.

    Args:
        ids (List[int]): List of ids to count (Your training/inference text, converted to ids)
        counts (Optional[Dict[int, int]]): Dictionary to update with counts.
    """
    # TODO: Implement this function
    return counts

def merge(ids: List[int], pair: Tuple[int, int], idx: int) -> List[int]:
    """
    Returns a new list of ids with the pair of ids now merged into one, using the 
    given idx as the new id.

    Args:
        ids (List[int]): List of ids to merge.
        pair (Tuple[int, int]): Pair of ids to merge.
        idx (int): New id for the merged pair.
    """
    newids: List[int] = []
    # TODO: Implement this function
    return newids