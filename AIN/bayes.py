# A function for calculating Bayes' theorem components
# Parameters:
#   pCause - probability of the cause
#   pEffectCause - probability of the effect given cause
#   pEffectNotCause - probability of the effect given not cause
def bayes(pCause, pEffectCause, pEffectNotCause):
  pNotCause = (1 - pCause) #p(-c)
  pNotEffectCause = 1 - pEffectCause #p(-e|c)
  pNotEffectNotCause = 1 - pEffectNotCause #p(-e|-c)

  print(f"P(c) = {pCause}")
  print(f"P(-c) = {pNotCause}")
  print(f"P(e|c) = {pEffectCause}")
  print(f"P(e|-c) = {pEffectNotCause}")
  print(f"P(-e|c) = {pNotEffectCause}")
  print(f"P(-e|-c) = {pNotEffectNotCause}")

  p1 = pEffectCause * pCause #p(e|c)*p(c)
  p2 = pEffectNotCause * pNotCause #p(e|-c)*p(-c)

  pCauseEffect = p1 / (p1 + p2) #p(c|e) = p(e|c)*p(c) / (p(e|c)*p(c) + p(e|-c)*p(-c))
  pNotCauseEffect = 1 - pCauseEffect #p(-c|e) = 1- p(c|e)
  print()
  print(f"P(c|e) = {pCauseEffect}")
  print(f"P(-c|e) = {pNotCauseEffect}")
  print(f"P(e) = {p1 + p2}")

  p3 = pNotEffectCause * pCause #p(-e|c)*p(c)
  p4 = pNotEffectNotCause * pNotCause #p(-e|-c)*p(-c)
  pCauseNotEffect =  p3 / (p3 + p4)
  pNotCauseNotEffect = 1 - pCauseNotEffect
  print()
  print(f"P(c|-e) = {pCauseNotEffect}")
  print(f"P(-c|-e) = {pNotCauseNotEffect}")
  print(f"P(c) = {p3 + p4}")

  pCorrect = pCause * pEffectCause + pNotCause * pNotEffectNotCause #p(c)*p(e|c) + p(-c)*p(-e|-c)
  pIncorrect = pCause * pNotEffectCause + pNotCause * pEffectNotCause #p(c)*p(e|c) + p(-c)*p(-e|-c)
  print()
  print(f"P(correct) = {pCorrect}")
  print(f"P(incorrect) = {pIncorrect}")


bayes(0.005, 0.95, 0.1)
