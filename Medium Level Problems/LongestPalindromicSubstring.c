int maxValue(int a, int b) {
    return a > b ? a : b;
}

int extend(char *s, int start, int end) {
    int length = strlen(s);
    while (start >= 0 && end < length) {
        if (*(s + start) != *(s + end)) {
            break;
        }
        start--;
        end++;
    }

    return end - start - 1;
}

char* longestPalindrome(char *s) {
    int max = 0, index = 0, length = strlen(s);
    for (int i = 0; i < length; ++i) {
        int evenLength = extend(s, i, i);
        int oddLength = extend(s, i, i + 1);
        if (max < maxValue(evenLength, oddLength)) {
            index = (evenLength > oddLength) ? (i - evenLength / 2) : (i - oddLength / 2 + 1);
            max = maxValue(evenLength, oddLength);
        }
    }

    char* longestPalindrome = malloc((max + 1) * sizeof(char));
    memcpy(longestPalindrome, &s[index], max);
    longestPalindrome[max] = '\0';
    return longestPalindrome;
}