import python
import semmle.code.python.dataflow.DataFlow

/**
 * Source : toute entrée utilisateur
 */
class UserInputSource extends TaintSource::FunctionCallNode {
  UserInputSource() { this.getName() = "input" }  // Python input()
}

/**
 * Sink : exécution SQL directe
 */
class SqlExecutionSink extends TaintSink::FunctionCallNode {
  SqlExecutionSink() { this.getName() = "execute" }  // cursor.execute()
}

/**
 * Flux de données : de l'entrée utilisateur vers l'exécution SQL
 */
from UserInputSource src, SqlExecutionSink sink, DataFlow::PathNode path
where DataFlow::localFlow(src, sink)
select sink, "Possible SQL injection: user input reaches execute()"