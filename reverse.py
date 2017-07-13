def count(dest,let):
    if len(dest) is 0:
        return 0
    if dest[0] is let:
        return 1+count(dest[1::], let)
    else:
        return count(dest[1::], let)

print str(count("s apdkho dahp adn dhapk adhassssess rs", 's'))
