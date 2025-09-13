import python

/**
 * Détecte l'utilisation de sqlite3.execute avec concaténation de chaîne
 */
from CallExpr call, Expr arg
where
  call.getTarget().hasName("execute") and
  arg = call.getArgument(0) and
  arg instanceof BinaryExpr
select call, "Potentiel SQL injection via concaténation de chaîne."
