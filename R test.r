'laba4 <- class(input_string)
    init <- function(self, input_string) {
        self.input_string <- input_string
    }
    split_string_to_chars <- function(self) {
        chars_list <- unlist(strsplit(self.input_string, split = ""))
        self.chars_list <- chars_list
        return(self.chars_list) 
    }
    index_counter <- function(self){
            final_symbols <- list()
            self.final_symbols <- final_symbols
            iter <- 0
            for (i in self.chars_list){
                if (iter < 50){
                iter = iter + 1
                pass
                }
                else{
                    append(final_symbols, i)
                }
            }
            return (self.final_symbols)
    }
    join_list_to_string <- function(self) {
  # Объединяем элементы списка в строку с пробелом между ними
        result_string <- paste(self.input_list, collapse = "")
        self.result_string <- result_string
        return(self.result_string)
    }
    reverse_words_in_string <- function(input_string) {
        # Разбиваем строку на слова
        words <- unlist(strsplit(input_string, " "))
        # Переворачиваем слова
        reversed_words <- rev(words)
        # Объединяем обратно в строку
        result_string <- paste(reversed_words, collapse = " ")
        self.result_string <- result_string
        return(self.result_string)
    }

test = laba4(первая половина                           вторая половина)
print (test)'
reverse_specific_words <- function(input_string) {
  # Функция для вычисления суммы порядковых номеров букв
  char_value_sum <- function(word) {
    return(sum(utf8ToInt(tolower(word)) - 96))
  }
  
  # Разбиваем строку на слова
  words <- unlist(strsplit(input_string, " "))
  
  # Переворачиваем только те слова, где сумма > 50
  modified_words <- sapply(words, function(word) {
    if (char_value_sum(word) > 50) {
      return(rev(strsplit(word, "")[[1]]))
    }
    return(word)
  })
  
  # Объединяем обратно в строку
  result_string <- sapply(modified_words, function(x) paste(x, collapse = ""))
  return(paste(result_string, collapse = " "))
}
result = reverse_specific_words('Сложная задача')
print (result)