def solution(s):
    result = 1001

    max_size = len(s) // 2

    for j in range(1,max_size+2):
        words = [s[i:i+j] for i in range(0, len(s), j)]

        last_word = ''
        multi = 1
        this_size = 0

        for h in range(len(words)):
            if last_word == words[h]:
                if multi == 1:
                    this_size += 1
                multi += 1
                last_word = words[h]
            else:
                if multi >= 10:
                    this_size += 1
                    if multi >= 100:
                        this_size += 1
                        if multi >= 1000:
                            this_size += 1

                multi = 1
                this_size += len(words[h])
                last_word = words[h]

        if multi >= 10:
            this_size += 1
            if multi >= 100:
                this_size += 1
                if multi >= 1000:
                    this_size += 1

        if this_size < result:
            result = this_size


    return result
