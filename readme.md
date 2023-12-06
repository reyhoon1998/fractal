\documentclass[12pt,a4paper]{article}
\usepackage{algorithm, algpseudocode, amsmath, amssymb, caption, csquotes, empheq, geometry, graphicx, hyperref, listings, multirow, physics, siunitx, subcaption, upgreek}
\usepackage[section]{placeins}
# Fractals
In this assignment we simulate some prominent fractals with determinstic and random approach.
 Fractals are self-similar patterns. My approach for deterministic algorithms is to consider a line, described by two points.
At each step, these points exposed to different mapping.
$\\begin{bmatrix} 
	a & b & c \\
	c & d & d\\
	e & f & g \\
	\end{bmatrix}
