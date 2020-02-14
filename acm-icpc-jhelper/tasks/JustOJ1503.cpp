#include "../library/header.hpp"

string node_type_func(string str) {
    bool all_0 = true;
    bool all_1 = true;
    for (int i = 0; i < str.length(); i++) {
        if ('0' == str[i]) {
            all_1 = false;
        }
        if ('1' == str[i]) {
            all_0 = false;
        }
    }
    if (all_0) {
        return "B";
    }
    if (all_1) {
        return "I";
    }
    return "F";
}

class FBITreeNode {
public:
    string fbi_str;
    string node_type;
    FBITreeNode *left;
    FBITreeNode *right;
};

class FBITree {
public:
    FBITreeNode *root;
    void build_tree (FBITreeNode *current_node, string fbi_str) {
        current_node->fbi_str = fbi_str;
        current_node->node_type = node_type_func(fbi_str);
        current_node->left = NULL;
        current_node->right = NULL;
        if (fbi_str.length() >= 2) {
            FBITreeNode *left_node = new FBITreeNode();
            FBITreeNode *right_node = new FBITreeNode();
            current_node->left = left_node;
            current_node->right = right_node;
            build_tree(current_node->left, fbi_str.substr(0, fbi_str.length() / 2));
            build_tree(current_node->right, fbi_str.substr(fbi_str.length() / 2, fbi_str.length()));
        }
    }

    string dfs_lfr(FBITreeNode *current_node) {
        string ans = "";
        if (current_node->left != NULL) {
            ans += dfs_lfr(current_node->left);
        }
        if (current_node->right != NULL) {
            ans += dfs_lfr(current_node->right);
        }
        ans += current_node->node_type;
        return ans;
    }
};

class JustOJ1503 {
public:
	void solve(std::istream& in, std::ostream& out) {
	    int n;
	    in >> n;
	    string fbi_str;
	    in >> fbi_str;
	    FBITree tree_instance;
	    tree_instance.root = new FBITreeNode();
	    tree_instance.build_tree(tree_instance.root, fbi_str);
	    out << tree_instance.dfs_lfr(tree_instance.root) << endl;
	}
};
