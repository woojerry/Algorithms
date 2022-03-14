this.$suggestions.querySelectorAll('li').forEach((el ,idx) => {
  if(el.classList === 'Suggestion__item--selected'){
      current = idx
      el.classList.remove('Suggestion__item--selected')
  }
}
  
this.$suggestions.querySelectorAll('li').forEach((el, idx) => {
  if(idx === current + 2){
      el.classList.add('Suggestion__item--selected')
  }
})



