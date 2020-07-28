// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

import java.util.*;

class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s) {
		int len = s.length();

		if (len == 0) {
			return True;
		}
		
		Stack<Character> st = new Stack<Character>();

		for (int i = 0; i < len; i++) {
			char ch = s.charAt(i);

			if (ch == '(') {
				st.push(ch);
			}

			if (ch == ')') {
				if (st.isEmpty()) {
					return False;
				}
				 
				if (st.peek() == '(') {
					st.pop();
				} else {
					return False;
				}
			}
		}
		
		return st.isEmpty();
	}

	public static void main(String[] args) {
		
	}
}