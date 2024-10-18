import math

def minimax(depth, nodeIndex, isMaximizingPlayer, values, maxDepth, alpha, beta):
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        print(f"Maximizer at depth {depth}")
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, values, maxDepth, alpha, beta)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Maximizer at depth {depth}, pruning with alpha: {alpha} and beta: {beta}")
                break
        print(f"Maximizer at depth {depth}, selected best: {best}")
        return best
    else:
        best = math.inf
        print(f"Minimizer at depth {depth}")
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, values, maxDepth, alpha, beta)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Minimizer at depth {depth}, pruning with alpha: {alpha} and beta: {beta}")
                break
        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best

maxDepth = 3
values = [-1, 4, 2, 6, -3, -5, 0, 7]
optimalValue = minimax(0, 0, True, values, maxDepth, -math.inf, math.inf)

print("\nThe optimal value is:", optimalValue)
