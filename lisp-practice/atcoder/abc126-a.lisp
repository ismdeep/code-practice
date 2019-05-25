(let ((n (read)) (k (read)) (s (read-line)))
	(setf (subseq s (- k 1) k) (string-downcase (subseq s (- k 1) k)))
	(format t "~A~%" s))